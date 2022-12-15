
def min_start (obj1_range,obj2_range)
    a = Integer(obj1_range[0])
    b = Integer(obj2_range[0])
    return a<b ? [obj1_range, obj2_range] : [obj2_range,obj1_range]
end

def max (a,b)
    return a>b ? a : b
end

def compare (obj1, obj2)
    obj1_range = obj1.split("-")
    obj2_range = obj2.split("-")
    first_obj,second_obj = min_start(obj1_range,obj2_range)
    if Integer(first_obj[1]) >= Integer(second_obj[0]) then
        return true
    end
    return false
    
end


num = 0
File.open('../input.txt','r')  do |f|
    f.each_line do |line|
        tasks = line.split(",")
        # puts tasks

        num += 1 if compare(tasks[0], tasks[1])                                                 
        
    end
    puts "result is:"+num.to_s()
end

