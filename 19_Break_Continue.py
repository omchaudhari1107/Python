for i in range(12):
    if i == 10:
        print("Skip the 10th iteration")
        continue  # skip the particular iteration 10
    print("5 *", i, "=", 5 * i)

print("-------------------------------")
for i in range(12):
    if i == 10:
        print("Skip the iterations after 10th one")
        break
    print("5 *", i, "=", 5 * i)
