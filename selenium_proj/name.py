
def get_sales_performance_feedback(sales_result, sales_target):
    ratio = int(sales_result) / int(sales_target)
    if ratio >= 1:
        return "A great result!"
    elif ratio > 0.75:
        return "You did not quite make it, but not too bad."
    elif ratio >= 0.5:
        return "Well, at least you tried"
    else:
        return "The boss wants to see you..."
# ui - slenium - bdd (cucumber)
#
# testng, pytest
# cucumber
#
# java selenium cucumber senerity serenity rest locust postman browser stack
#
# back end - rest api - request, rest assured - bdd
#
# mobile - appium
