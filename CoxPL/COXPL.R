rm(list=ls())
library(survival)
library(knitr)

########################################################################################################3
# Log partial likelihood for the Cox proportional hazards model
########################################################################################################
# X      : design matrix
# status : vital status (1 - dead, 0 - alive)
# times  : survival times
# n.obs  : number of observed events

# Risk set function
risk.set <- function(t) which(times >= t)

# log partial likelihood function
log.parlik <- function(beta){
  status <- as.vector(as.logical(status))
  Xbeta <- as.vector(X%*%beta)
  lpl1 <- sum(Xbeta[status])
  temp <- vector(   )
  for(i in 1:n.obs) temp[i] <- log(sum(exp(Xbeta[rs[[i]]])))
  lpl2 <- sum(temp)
  return(-lpl1 + lpl2)
}

###########################################################################################################
# Example 1 : Ovarian Cancer Survival Data
# ?ovarian
###########################################################################################################
# Required variables
X <- cbind(ovarian$age, ovarian$ecog.ps)
status <- ovarian$fustat
times <- ovarian$futime
n.obs <- sum(status)

# Risk set
rs <- apply(as.matrix(times[as.logical(status)]), 1, risk.set)

# Optimisation step
OPT <- optim(c(0,0),log.parlik, control = list(maxit = 1000))

# Using the survival R package
fit <- coxph(Surv(futime, fustat) ~ age + ecog.ps, data=ovarian)

# Comparison
MAT <- cbind( OPT$par,fit$coefficients)
colnames(MAT) <- c("survival package", "MPLE")
kable(MAT, digits = 4)


###########################################################################################################
# Example 2 : NCCTG Lung Cancer Data
# A missing observation is removed
# ?lung
###########################################################################################################
# Required variables
X <- cbind(lung$age, lung$sex, lung$ph.ecog)[-14,]
status <- lung$status[-14] - 1
times <- lung$time[-14]
n.obs <- sum(status)

# Risk set
rs <- apply(as.matrix(times[as.logical(status)]), 1, risk.set)

# Optimisation step
OPT <- optim(c(0,0,0),log.parlik, control = list(maxit = 1000))

# Using the survival R package
fit <- coxph(Surv(time, status) ~ age + sex + ph.ecog, data=lung)

# Comparison
MAT <- cbind( OPT$par,fit$coefficients)
colnames(MAT) <- c("survival package", "MPLE")
kable(MAT, digits = 4)


###########################################################################################################
# Example 3 : Veterans' Administration Lung Cancer study
# ?veteran
###########################################################################################################
# Required variables
X <- cbind(veteran$age, veteran$karno, veteran$trt)
status <- veteran$status
times <- veteran$time
n.obs <- sum(status)

# Risk set
rs <- apply(as.matrix(times[as.logical(status)]), 1, risk.set)

# Optimisation step
OPT <- optim(c(0,0,0),log.parlik, control = list(maxit = 1000))

# Using the survival R package
fit <- coxph(Surv(time, status) ~ age + karno + trt, data=veteran)

# Comparison
MAT <- cbind( OPT$par,fit$coefficients)
colnames(MAT) <- c("survival package", "MPLE")
kable(MAT, digits = 4)