# Program to calculate time saved by speeding

def time_saved(avg_speed, speed_limit, distance):
    time_at_speed_limit = distance / speed_limit  # hours
    time_at_avg_speed = distance / avg_speed      # hours
    saved_hours = time_at_speed_limit - time_at_avg_speed
    saved_minutes = saved_hours * 60
    return saved_minutes

# Example run
avg_speed = float(input("Enter average speed (mph): "))
speed_limit = float(input("Enter speed limit (mph): "))
distance = float(input("Enter distance traveled (miles): "))

saved_minutes = time_saved(avg_speed, speed_limit, distance)

print(f"\nTime saved: {saved_minutes:.0f} minutes")
