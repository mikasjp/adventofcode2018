data = File.open("data.txt")
                .read()
                .split("\n")
                .map(&:to_i)

# first part
puts "First part: " + data.inject(0, &:+).to_s

# second part
duplicates = Hash.new
$freqency = 0

data.cycle do |x|
    $freqency += x
    break if duplicates.has_key?($freqency)
    duplicates.store($freqency, TRUE)
end

puts "Second part: " + $freqency.to_s