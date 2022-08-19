library(ggplot)

ingredient <- read.csv("~/Desktop/Jobs and Qualifications/PreScreen_r3/ingredient.csv")
summary(ingredient) #Descriptive analysis of each ingredient

#Aim: Want to check if the formulations are significantly different 
boxplot(ingredient)
par(mfrow=c(3,3))

#Names associated (Column Names)
name <- names(ingredient) ;name

#Reformatting data into groups 
dat <- unlist(ingredient, use.names = FALSE) ; dat
dat_1 <- matrix(dat,nrow=length(dat),ncol=1) ; dat_1

dat_name <-c()
for (i in name){
  
  dat_name <- append(dat_name,values = rep(i, length(ingredient$a))) 
  
}
dat_name_1 <- matrix(dat_name,nrow=length(dat_name),ncol=1)

new_dat <- cbind(dat_1, dat_name_1) ; new_dat

#Plots
qqnorm(ingredient$a)
qqline(ingredient$a)
hist(ingredient$a)

qqnorm(ingredient$b)
qqline(ingredient$b)
hist(ingredient$b)

qqnorm(ingredient$c)
qqline(ingredient$c)
hist(ingredient$c)

qqnorm(ingredient$d)
qqline(ingredient$d)
hist(ingredient$d)

qqnorm(ingredient$e)
qqline(ingredient$e)
hist(ingredient$e)

qqnorm(ingredient$f)
qqline(ingredient$f)
hist(ingredient$f)

qqnorm(ingredient$g)
qqline(ingredient$g)
hist(ingredient$g)

qqnorm(ingredient$h)
qqline(ingredient$h)
hist(ingredient$h)

qqnorm(ingredient$i)
qqline(ingredient$i)
hist(ingredient$i)

#Parametric test requires assumption of normality, if fail use non-parametric test

# H0 : Formulations are NOT significantly different
# H1 : Formulations are significantly different
# Since some data fail the assumption of normality, we can do transformation and then perform ANOVA test
#
kruskal.test(new_dat[,1]~new_dat[,2],data=ingredient)
