# same global solution for both #3633 and #3635
# we cannot brute force this one
# need to try to go land first then water, then later try to go water first then land
# in each trial, we need to store several things
# first, iterate the endtime of the chosen first ride
# pre-calculate min duration if the endtime is higher than starttime of the second ride
# because in this case, the total endtime = first endtime + second duration
# the other case with total endtime = second endtime when second starttime > first endtime
# also pre-calculate it for quick lookup
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def go_a_to_b(aStartTime, aDuration, bStartTime, bDuration):
            a_sorted = sorted(s + d for s, d in zip(aStartTime, aDuration))

            b_sorted = sorted((s, d) for s, d in zip(bStartTime, bDuration))
            n = len(b_sorted)

            bd_min_p = []
            for i in range(n):
                _, bd = b_sorted[i]
                if not bd_min_p or bd_min_p[-1] > bd:
                    bd_min_p.append(bd)
                else:
                    bd_min_p.append(bd_min_p[-1])

            be_min_p = []
            for i in range(n):
                bs, bd = b_sorted[~i]
                be = bs + bd
                if not be_min_p or be_min_p[-1] > be:
                    be_min_p.append(be)
                else:
                    be_min_p.append(be_min_p[-1])
            
            j = 0
            ans = float("inf")
            for ae in a_sorted:
                while j < n:
                    bs, bd = b_sorted[j]
                    if bs >= ae:
                        break
                    j += 1
                if j > 0:
                    ans = min(ans, ae + bd_min_p[j-1])
                if j < n:
                    ans = min(ans, be_min_p[~j])
            
            return ans

        ans = min(
            go_a_to_b(landStartTime, landDuration, waterStartTime, waterDuration),
            go_a_to_b(waterStartTime, waterDuration, landStartTime, landDuration)
        )
        return ans

# lee's optimal solution is crazy
# explanation: "Calculates the earliest possible time to finish all land tasks.
# Calculates the earliest possible time to finish all water tasks.
# Finds the earliest finish time for the "water-first, then land" sequence.
# Finds the earliest finish time for the "land-first, then water" sequence."
# this is why math is important
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = min(s + d for s, d in zip(landStartTime, landDuration))
        water = min(s + d for s, d in zip(waterStartTime, waterDuration))
        water_land =  min(max(s, water) + d for s, d in zip(landStartTime, landDuration))
        land_water =  min(max(s, land) + d for s, d in zip(waterStartTime, waterDuration))
        return min(water_land, land_water)