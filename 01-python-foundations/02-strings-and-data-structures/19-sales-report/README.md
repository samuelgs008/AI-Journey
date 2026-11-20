# 19 - Sales Report

A sales spreadsheet saved as CSV text. The columns can come in any order, and some rows are broken. Read it **safely** and build a report. This is the job you'll later do with pandas, done by hand so you know what happens inside.

## Input

The first line is the **header**: the column names, separated by commas. It always has the columns `date`, `seller`, `product`, `qty` and `price`, in **any order**, and it may have extra columns. Then come the data rows, until a line with `END`. There may be spaces around any value.

`date` is `YYYY-MM-DD`, `qty` is a whole number of units and `price` is the price of one unit, with a `.` for decimals.

## Output

A row is **skipped** when it doesn't have the same number of fields as the header, when `qty` is not a whole number, or when `price` is not a number. The value of a sale is `qty × price`.

```
TOTAL = <total value of all sales>
BY SELLER:
  <seller>  <value>  <share of the total>
BEST PRODUCT = <product> (<n> units)
BY MONTH:
  <YYYY-MM>  <value>
SKIPPED = <n> rows (lines a, b, ...)
```

- Money uses a thousands separator and 2 decimal places (`1,504.80`).
- **BY SELLER**: from the highest value (ties: alphabetical order). 2 spaces, the seller left-aligned in 10, the value right-aligned in 12, the share right-aligned in 8 as a percentage with 1 decimal place.
- **BEST PRODUCT**: the product with the most units sold (ties: alphabetical order).
- **BY MONTH**: in date order. 2 spaces, the month, the value right-aligned in 12.
- **SKIPPED**: line numbers count from 1, and the header is line 1. If no row was skipped, print `SKIPPED = 0 rows`.

There is always at least one valid row.

## Samples

<table>
<tr><th>Sample Input</th><th>Sample Output</th></tr>
<tr>
<td><pre>
date,seller,product,qty,price
2026-01-15, Ana, mouse, 10, 25.00
2026-01-20,Bruno,keyboard,2,150.00
2026-02-03,Ana,keyboard,1,150.00
2026-02-10,Caio,mouse,4,25.00
END
</pre></td>
<td><pre>
TOTAL = 800.00
BY SELLER:
  Ana             400.00   50.0%
  Bruno           300.00   37.5%
  Caio            100.00   12.5%
BEST PRODUCT = mouse (14 units)
BY MONTH:
  2026-01      550.00
  2026-02      250.00
SKIPPED = 0 rows
</pre></td>
</tr>
<tr>
<td><pre>
price, qty, seller, date, product, store
99.90,2,Ana,2026-03-01,headset,north
10,abc,Bruno,2026-03-02,cable,south
5.5,10,Bruno,2026-03-02,cable,south
1.000,1,Ana,2026-03-05,mouse
1250.00,1,Bruno,2026-04-01,monitor,north
END
</pre></td>
<td><pre>
TOTAL = 1,504.80
BY SELLER:
  Bruno         1,305.00   86.7%
  Ana             199.80   13.3%
BEST PRODUCT = cable (10 units)
BY MONTH:
  2026-03      254.80
  2026-04    1,250.00
SKIPPED = 2 rows (lines 3, 5)
</pre></td>
</tr>
</table>

<details>
<summary>💡 Hints (try on your own first!)</summary>

1. The header tells you **where** each column is. Build a dictionary column name → index: `{"price": 0, "qty": 1, ...}`. `enumerate` from exercise 15 does it in one comprehension. Then `fields[col["qty"]]` works whatever the order.
2. Strip every field: `[f.strip() for f in line.split(",")]`.
3. `"10".isdigit()` checks `qty`. For `price`, a number with at most one dot: remove **one** dot with `.replace(".", "", 1)` and check `.isdigit()` on what's left.
4. Count the line numbers yourself. The header is line 1, so the first data row is line 2.
5. Three counting dictionaries (seller → value, product → units, month → value) do almost all the work. The month is a slice of the date.
6. Line 5 of sample 2 has only 5 fields, but the header has 6. That's why it's skipped, even though everything in it looks fine.
7. `f"{1305.0:>12,.2f}"` gives `    1,305.00`.
8. In real life, `float` is not good for money: try `0.1 + 0.2`. In Level 04 you'll meet `decimal`, which fixes it.

</details>
