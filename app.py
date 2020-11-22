import os
import te
if os.path.exists('customer.db'):
	print('database exists')
else:
	print('database does not exist')
#te.delete_one('7')
#now add many records
lst = [
        ('Brenda','Leone','Brenda@gmail.com'),
        ('Selena','gomez','selena@gmail.com')
      ]
#te.add_many(lst)
te.email_lookup('john@codemy.com')
#showing all the records
#te.show_all()

