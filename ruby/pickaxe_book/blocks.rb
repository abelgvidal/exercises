def two_times
	yield
	yield
end

two_times do
	#puts "hey"
end


def fib_up_to(max)
	i1, i2 = 1, 1
	while i1 <= max 
		yield i1
		i1, i2 = i2, i1+i2
	end
end


class Array
	def find
		each do |value|
			return value if yield(value)
		end
		nil
	end
end

#(30...50).each.with_index { |value, index| puts "(#{index}) -> #{value}"}


triangular_numbers = Enumerator.new do |yielder|
  number = 0
  count = 1
  loop do
    number += count
    count += 1
    yielder.yield number
  end
end

5.times {  print triangular_numbers.next, " " }
