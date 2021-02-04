has_high_income = True
has_good_credit = False
has_criminal_record = True

if has_high_income and has_good_credit and not has_criminal_record:
    print("(and statement) Eligibale for loan")
else:
    print("(and statement) Not")

if (has_high_income or has_good_credit) and not has_criminal_record:
    print("(or statement) Eligibale for loan")
else:
    print("(or statement) Not")