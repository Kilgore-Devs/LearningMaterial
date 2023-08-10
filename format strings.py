# you can format strings with format()
# there are parts of text that you don't control, database, user inputs etc.
# To control those values you would add placeholders using {} in the text,
# Then run the values through the format method.

price = 100
text = "This is {} dollars."
print(text.format(price))

# Add parameters inside {} to specify how to convert the value, see a larger list of formats at the end.

price2 = 100
text2 = "This is {:.2f} dollars"  # formats as a fix point
print(text2.format(price2))

# Multiple values
quantity = 10
item_number = 5
price = 69
order = "I would like {} of item number {} for {:.2f} dollars"
print(order.format(quantity, item_number, price))

# Index numbers inside {}, make sure values are plaed in the correct placeholders.
amount = 5
itemnum = 333
cost = 300
neworder = "Give me {0} of item number {1} for {2:.2f} dollars."  # can index multiple times if needed.
print(neworder.format(amount, itemnum, cost))


# Naming indexes is possible. Put name inside {} like {name}.
# Must use names when pass the parameter values. txt.format(name = Ryan).
carorder = "I would like to buy a {type} {make} {model}."
print(carorder.format(type= "used", make = "Dodge", model = "Viper SRT-10"))

"""                 Formatting Types
Inside placeholders add formatting types to format the result:

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format """