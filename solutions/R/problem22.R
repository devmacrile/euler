"
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score. For example, 
when the list is sorted into alphabetical order, COLIN, which is worth 3 + 
15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
score of 938  53 = 49714. What is the total of all the name scores in the file?
"

setwd("/Users/rileyde/Documents/projects/euler/data")
names = read.csv("names.txt", header=F)
names[which(is.na(names) == T)] <- "N A" 
names = sort(names)

# list mapping letters onto 'scores'
# score is which letter of the alphabet it is
letterScores = list()
for(i in 1:26){
    letterScores[LETTERS[i]] = i
}
letterScores[" "] = 0  # just in case??


nameScore = function(name){
    # i.e. COLIN = 3 + 15 + 12 + 9 + 14 = 53
    if(name == "N A") return(15)
    score = 0
    name = strsplit(name, split="")
    for(i in name[[1]]){
        score = score + letterScores[[i]]
    }
    return(score)
}

start = proc.time()

# calculate name score for each name
nscores = rep(0, length(names))
for(i in 1:length(names)){
    nscores[i] = nameScore(as.character(names[[i]]))
}

# name sort index
index <- c(1:length(names))

nameAndScore <- data.frame(t(as.vector(names)))
nameAndScore <- cbind(cbind(nameAndScore, index), nscores)
totalNameScores = apply(nameAndScore[,c(2,3)], 1, prod)

elapsed = proc.time() - start
cat(paste("The solution is ", sum(totalNameScores), ", found in ", elapsed[[3]], " seconds", sep=""))
# The solution is 871198282, found in 0.548999999882653 seconds






