rm(list=ls())
# Required packages
library(survival)
library(flexsurv)

# lung cancer data set
data(lung)
?lung
head(lung)


# Survival model using a Weibull distribution
fit.weibull <- flexsurvreg(formula = Surv(time, status) ~ 1, data = lung,
                           dist = "weibull")

fit.weibull

# Survival model using a Weibull distribution
fit.lnorm <- flexsurvreg(formula = Surv(time, status) ~ 1, data = lung,
                         dist = "lognormal")

fit.lnorm

# Survival model using a Generalised Gamma distribution
fit.ggama <- flexsurvreg(formula = Surv(time, status) ~ 1, data = lung,
                         dist = "gengamma")

fit.ggama

# Comparison of survival functions
plot.new()
plot.window(xlim = c(0,1000), ylim = c(0,1))
axis(1, cex.axis = 1.5); axis(2, cex.axis = 1.5); box(); title(ylab="Survival", xlab="Time", cex.lab = 1.5)
lines(fit.weibull, col="red", lwd.ci=0, lty.ci=1)
lines(fit.lnorm, col="blue", lwd.ci=0, lty.ci=1)
lines(fit.ggama, col="green", lwd.ci=0, lty.ci=1)
legend("topright", legend = c("weibul", "lnorm", "gengamma"),
       lty = 1, col = c("red","blue","green"))


# Comparison of hazard functions
plot.new()
plot.window(xlim = c(0,1000), ylim = c(0,0.007))
axis(1, cex.axis = 1.5); axis(2, cex.axis = 1.5); box(); title(ylab="Hazard", xlab="Time", cex.lab = 1.5)
lines(fit.weibull, col="red", lwd.ci=0, lty.ci=1, type = "hazard")
lines(fit.lnorm, col="blue", lwd.ci=0, lty.ci=1, type = "hazard")
lines(fit.ggama, col="green", lwd.ci=0, lty.ci=1, type = "hazard")
legend("topright", legend = c("weibul", "lnorm", "gengamma"),
       lty = 1, col = c("red","blue","green"))

# Comparison of the three models using AIC
AIC(fit.weibull)
AIC(fit.lnorm)
AIC(fit.ggama)



# Comparison of survival functions and KM estimator
plot(fit.weibull, col="red", lwd.ci=0, lty.ci=1, ylab="Survival", xlab="Time", cex.lab = 1.5,cex.axis = 1.5)
lines(fit.lnorm, col="blue", lwd.ci=0, lty.ci=1)
lines(fit.ggama, col="green", lwd.ci=0, lty.ci=1)
legend("topright", legend = c("weibul", "lnorm", "gengamma", "KM"),
       lty = 1, col = c("red","blue","green","black"))

