"""PSCP Program"""
def main() -> int:
    """Circular I"""
    point_q1, point_q2 = float(input()), float(input())
    radius = float(input())
    point_p1, point_p2 = float(input()), float(input())
    distance = (((point_q1 - point_p1)**2) + ((point_q2 - point_p2)**2))**(1/2)
    if distance <= radius:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == "__main__":
    main()
