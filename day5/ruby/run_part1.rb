
$stack_1 = ['B','Z','T']
$stack_2 = ['V','H','T','D','N']
$stack_3 = ['B','F','M','D']
$stack_4 = ['T','J','G','W','V','Q','L']
$stack_5 = ['W','D','G','P','V','F','Q','M']
$stack_6 = ['V','Z','Q','G','H','F','S']
$stack_7 = ['Z','S','N','R','L','T','C','W']
$stack_8 = ['Z','H','W','D','J','N','R','M']
$stack_9 = ['M','Q','L','F','D','S']
$stack = [$stack_1,$stack_2,$stack_3,$stack_4,$stack_5,$stack_6,$stack_7,$stack_8,$stack_9]


$stack_1 = ['Z','N']
$stack_2 = ['M','C','D']
$stack_3 = ['P']
$stack = [$stack_1,$stack_2,$stack_3]
# $stack = [['Z','N'],['M','C','D'],['P']]

# $stack = Hash["1"=>$stack_1,"2"=>$stack_2,"3"=>$stack_3]
def move_crates (num, from, to)
    from_index = from - 1
    to_index = to - 1
    from_stack = $stack[from_index]
    puts "/////////#{$stack[from_index]}////////"
    # 测试第二次的时候，数组会没有正常pop，不知道为啥。。卡了好几天囧。用python解决了
    $stack[from_index].each do |el|
        if num > 0 then
            trans_data = $stack[from_index].pop()
            puts "\t[#{num}]:now the data is #{trans_data},el is #{el}\n"
            $stack[to_index] << trans_data
            num -= 1
            puts "\t\t[-]num is #{num}(#{num-1>=0})|#{from_stack}\n"
        end
    end
    puts $stack[from_index]

    # puts "Stack[#{from}] #{$stack[from_index]} Stack[#{to}] #{$stack[to_index]}"

end


puts "1:#{$stack_1}\n2:#{$stack_2}\n3:#{$stack_3}\n"
File.open('../input.txt','r') do |f|
    f.each_line do |line|
        puts line
        move_num = Integer(line.split(' ')[1])
        from = Integer(line.split(' ')[3])
        to = Integer(line.split(' ')[-1])
        move_crates(move_num, from, to)
        puts "1:#{$stack_1}\n2:#{$stack_2}\n3:#{$stack_3}\n"

        
    end
    # puts "#{$stack_1[0]},#{$stack_2[0]},#{$stack_3[0]},#{$stack_4[0]},#{$stack_5[0]},#{$stack_6[0]},#{$stack_7[0]},#{$stack_8[0]},#{$stack_9[0]}"

    # puts "#{$stack_1[0]},#{$stack_2[0]},#{$stack_3[0]}"


end 


# test = [1,2,3]
# puts test.pop()
# test[0] = 666
# puts test