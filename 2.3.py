
#\t \n ;lower 全小写,upper全大写，title单词首字大写
name = 'ryan'
first_name = 'shi'
full_name = name+ '\''+'\t' + first_name
print(full_name)
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

#针对strip的详细解释，翻译过来，就是：
#对于输入的字符串，去除，开始的，和，末尾的，字符；
#所要去除的字符，是你通过参数chars所指定的。
#如果不指定该参数，或者为None，即删除空格
message= ' Albert erist onece said,"a person who never made a mistake never tried anything new."  '
print(message.strip(' Albert'))
print(message.lstrip(' Albert'))
print(message.rstrip(' new."'))
