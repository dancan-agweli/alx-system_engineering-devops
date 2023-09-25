# Open a CSV file for writing
with open("{}.csv".format(u_id), "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    
    # Write a header row to the CSV file
    writer.writerow(["User ID", "Username", "Completed", "Title"])

    # Write each to-do item to the CSV file
    for t in todos:
        row = [u_id, username, t.get("completed"), t.get("title")]
        writer.writerow(row)

