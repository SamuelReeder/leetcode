class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # greedy problem
        # sort ascending and hurdle asteroids at it
        # sum doesnt work because there could be a large asteroid

        asteroids = sorted(asteroids)

        for a in asteroids:
            if mass < a:
                return False

            mass += a

        return True
