
inputfile = "input/Day6Input.txt"

print("Advent of Code 2020 - Day 6")
with open(inputfile, 'r') as f:
	groups = f.read().split("\n\n")
	
totals_pt1, totals_pt2 = [], []
	
for group in groups:
	group_sum_pt1, group_sum_pt2 = 0, 0
	group_ans = "".join(group).replace("\n","")
	for i in range(ord('a'), ord('z')+1):
		# Part 1
		group_sum_pt1 += 1 if chr(i) in group_ans else 0
		# Part 2
		group_sum_pt2 += 1 if group_ans.count(chr(i)) == group.count("\n")+1 else 0
	
	totals_pt1.append(group_sum_pt1)
	totals_pt2.append(group_sum_pt2)
	
print("Part 1:", sum(totals_pt1))
print("Part 2:", sum(totals_pt2))
