# Count Elements Greater Than Previous Average

responsetimes = [100,200,300]

def countResponseTimeRegressions(response_times):
    count = 0
    for i in range(len(response_times)):
        if i > 0:
            average = int(sum(response_times[:i])/i)
            if response_times[i] > average:
                count = count+1
    return count


print(countResponseTimeRegressions(responsetimes))