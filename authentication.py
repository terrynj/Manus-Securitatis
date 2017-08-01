r=open("Lengths.txt","r")

user_name = input("Who are you? ")

print("Enter your finger lengths.")

# input_lengths = [0, 0, 0, 0, 0]
# for i in range(5):
#     input_lengths[i] = input("Enter finger length " + str(i+1))

finger_to_read = -1
finger_profile = [0, 0, 0, 0, 0]
for current_line in r:
    if finger_to_read != -1 and finger_to_read < 5:
        finger_profile[finger_to_read] = int(current_line)
        finger_to_read += 1

    print(user_name)
    print(current_line)
    if user_name == current_line:
        print("YEAH")
        finger_to_read = 0


print(user_name)
print(finger_profile)

print("Authorized.")

r.close()