
def min (a,b) 
    return a<b ? a : b
end

def max (a,b)
    return a>b ? a : b
end

def compare (obj1, obj2)
    obj1_range = obj1.split("-")
    obj2_range = obj2.split("-")
    res_head = Integer(obj1_range[0]) - Integer(obj2_range[0])
    res_end = Integer(obj1_range[1]) - Integer(obj2_range[1])
    puts "%s * %s " % [res_head,res_end]
    if res_head * res_end ==0 then
        # puts "test %s,  %s" % [obj1,obj2]
        return true
    elsif res_head * res_end < 0 then
        # puts "test %s,  %s" % [obj1,obj2]
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

