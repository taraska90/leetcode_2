days = set(["monday", "tuesday"])
month = {"february", "january"}

daysa = set(["Mon","Tue","Wed"])
daysb = set(["Wed","Thu","Fri","Sat","Sun"])


daysa | daysb
# union
# {'Sun', 'Wed', 'Thu', 'Tue', 'Mon', 'Sat', 'Fri'}
daysa & daysb
# intersection
# {'Wed'}
daysa - daysb
# difference
# {'Tue', 'Mon'}
# результатом будут элементы, которые есть в первом сете, но нет во втором
# так как Wed есть и во втором наборе тоже, его не окажется в резлультате