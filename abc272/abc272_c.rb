n = gets.to_i
a = gets.split.map(&:to_i).sort.reverse

e = a.select{ |factor| factor.even? }.sort[-2..] || [-1]
o = a.select{ |factor| factor.odd? }.sort[-2..] || [-1]

puts [e.sum, o.sum].max
