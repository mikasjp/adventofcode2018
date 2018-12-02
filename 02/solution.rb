data = File.open("data.txt")
    .read()
    .split

# First part
c =  data.map{|row| row.split("")}
            .map{|row| row.uniq.map{ |char| row.count(char) if row.count(char)!=1 }.compact.uniq}
            .reduce([], :concat)

puts "First part: " + c.uniq
        .map{|x| c.count(x)}
        .inject(:*).to_s