import polars as pl
from thefuzz import process


# The original name list
correct_names_list = pl.read_excel(
    "data/name.xlsx", sheet_name="Correct Names"
).with_columns(
    [
        pl.col("First").fill_null(""),
        pl.col("Initial").fill_null(""),
        pl.col("Last Name").fill_null("")
    ]
).with_columns(
    ((pl.col("First")) + " " + (pl.col("Initial")) + " " +
     pl.col("Last Name")).alias("Full Name")
).select("Full Name").to_series()



# The name inputs when use to lookup
mistreated_names_df = pl.read_excel(
    "data/name.xlsx", sheet_name="Mistreated Names"
)

# Fuzzy Name Search
matched_names = []
match_certainty = []

mistreated_names_list = mistreated_names_df.select("Mistreated").to_series()

for input_name in mistreated_names_list:
    match = process.extractOne(input_name, correct_names_list)
    matched_names.append(match[0])
    match_certainty.append(match[1])

# a = process.extractOne(mistreated_names_list[3], correct_names_list)
# print(mistreated_names_list[3])
# print(a[0])


# print(matched_names)
# print(match_certainty)


# Reorganize the original name list using the idexes from excel
# Compare reordered list with matched list from fuzzy search

correct_names_checker = []

for n in mistreated_names_df.select("Source Row").to_series():
    correct_names_checker.append(correct_names_list[n-2])
    # print(correct_names_checker)


print(correct_names_checker == matched_names)


# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = [3, 2, 1]
# print(list1 == list2)  # True
# print(list1 == list3)  # False
