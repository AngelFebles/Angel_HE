import polars as pl

#  a1i0p0s0t0

# placeholder vals for tests
family_type = {
    "`Adult(s)`": 1,
    "`Infant(s)`": 0,
    "`Preschooler(s)`": 0,
    "`Schoolager(s)`": 0,
    "`Teenager(s)`": 0
}
housing_type = "Efficiency"
food_plan = "Thrifty"


def get_coefficients(housing_type, food_plan, **family_type):

    coefficients_df = pl.read_excel(r"data\coefficients.xlsx")

    list_of_vals = []

    for row in coefficients_df.rows(named=True):
        value = row["(Intercept)"] + (
            (row["`Adult(s)`"] * family_type["`Adult(s)`"]) +
            (row["`Infant(s)`"] * family_type["`Infant(s)`"]) +
            (row["`Preschooler(s)`"] * family_type["`Preschooler(s)`"]) +
            (row["`Schoolager(s)`"] * family_type["`Schoolager(s)`"]) +
            (row["`Teenager(s)`"] * family_type["`Teenager(s)`"])
        )
        list_of_vals.append(value)
    # print(list_of_vals)

    new_df = coefficients_df.select(pl.col("output")
                                    ).with_columns(
                                        pl.Series("values", list_of_vals)
    )

    # For when theres only adults, put childcare cost at 0
    if (
        family_type["`Infant(s)`"] == 0 and
        family_type["`Preschooler(s)`"] == 0 and
        family_type["`Schoolager(s)`"] == 0 and
        family_type["`Teenager(s)`"] == 0
    ):
        new_df = new_df.with_columns(
            pl.when(pl.col("output") == "Child Care Costs")
            .then(0)
            .otherwise(pl.col("values"))
            .alias("values")
        )

    # print(new_df)

    food_n_housing = pl.DataFrame({
        "output": ["housing_cost", "food_cost"],
        "values": [get_housing_cost(housing_type),
                   get_food_costs(food_plan, **family_type)],
    }, strict=False)

    new_df = new_df.vstack(food_n_housing)

    # print(new_df)

    return new_df


def get_food_costs(food_plan, **family_type):
    food_df = pl.read_excel(r'data\food_plans_means.xlsx')

    food_df = food_df.select(["age_group", food_plan])

    cost_per_group = food_df.select(food_plan).transpose(
        column_names=food_df["age_group"]
    )

    result = (
        cost_per_group["Adult"][0] * family_type["`Adult(s)`"] +
        cost_per_group["Infant"][0] * family_type["`Infant(s)`"] +
        cost_per_group["Preschooler"][0] * family_type["`Preschooler(s)`"] +
        cost_per_group["School Age"][0] * family_type["`Schoolager(s)`"] +
        cost_per_group["Teenager"][0] * family_type["`Teenager(s)`"]
    )

    # result = (cost_per_group.select(pl.col("Adult"))
    #           ).row(0)

    return result


def get_housing_cost(housing_type):
    housing_df = pl.read_excel(r"data\housing_cost.xlsx")

    cost = housing_df.filter(pl.col("housing_type") ==
                             housing_type).select("housing_cost").item()

    return cost


family_costs = get_coefficients(housing_type, food_plan, **family_type)


# food_costs = get_food_costs("Thrifty", **family_type)

# get_housing_cost("Efficiency")

# family_costs.write_json("data/family_costs.json")
