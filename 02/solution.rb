DATA = File.open("data.txt")
    .read()
    .split

# First part
c =  DATA.map{|row| row.split("")}
            .map{|row| row.uniq.map{ |char| row.count(char) if [2, 3].include? row.count(char) }.compact.uniq}
            .reduce([], :concat)

puts "First part: " + c.uniq
        .map{|x| c.count(x)}
        .inject(:*).to_s

# Second part

def hamming(p)
    h = p[0].split("").zip(p[1].split("")).map{|p| p.first==p.last}
    return h.count(FALSE), h.each_with_index.select{|v,i| v==FALSE}.map{|p| p[1]}
end

puts "Second part: " + DATA.combination(2)
            .map{ |p| [p[0], hamming(p)[1]] if hamming(p)[0]==1 }
            .compact
            .map{|p| p.first.split("").each_with_index.select{|v,i| i!=p.last.last}.map{|q| q[0]}}
            .first
            .join("")