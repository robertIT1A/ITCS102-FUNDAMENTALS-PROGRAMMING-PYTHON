# Anime list
# Using list operations
print("Anime Title List")

anime_list = [] # empty list
proceed = True   

while proceed == True:
    anime = input("Enter the title of an Anime (or type 'end' to end): ")
    if anime == "end": # stopper
        print("All done,You are now exiting!! ")
        break    # terminate the loop

    else: # proceed
        print(f"'{anime}' added to the your Anime List") # every time that you answer, it will show up unless the user type "end"
        anime_list.append(anime) # all title that the user enter will be go to empty list

print(f"Here All the Title of your Anime:") # after user type "end" it will show up
for i in anime_list:     # print all the anime that the user enter
    print(f"- {i}")