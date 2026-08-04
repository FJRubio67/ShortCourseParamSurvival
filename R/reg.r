rm(list=ls())
# Required packages
library(survival)
library(flexsurv)
library(eha)

# lung cancer data set
data(lung)
?lung
head(lung)

# AFT model using a lognormal baseline distribution
fit.aft <- aftreg(formula = Surv(time, status) ~ age + sex, data = lung,
                         dist = "lognormal")
# PH model using a lognormal baseline distribution
fit.ph <- phreg(formula = Surv(time, status) ~ age + sex , data = lung,
                dist = "lognormal")

# Comparison of the three models using AIC
AIC.aft <- -2*(fit.aft$loglik[2]) + 2*length(fit.aft$coefficients)
AIC.ph <- -2*(fit.ph$loglik[2]) + 2*length(fit.ph$coefficients)

AIC.aft
AIC.ph

# Comparison 
plot(fit.aft)
plot(fit.ph)

