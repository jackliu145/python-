def my_printj(name, age, *args, city, job):
    print('name:%s, age:%s, city:%s, job:%s' % (name, age, city, job))
    print(city)
    print(job)
    print(args)


my_printj('jack', 12, city="Jingzhou", job="java" )

kw = {'city':"Jingzhou", 'job':"java"}
my_printj('marry', 22, **kw)


my_printj('marry', 22, **{'city':"Jingzhou", 'job':"java"})
