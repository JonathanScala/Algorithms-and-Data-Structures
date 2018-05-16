class Sorting:
    @staticmethod
    def radix_sort(L):
        if len(L) == 0:
            return []

        bins = [list() for i in range(10)]
        main = L[:]
        digit = 1
        Max = max(main)

        while (Max > digit):
            for i in main:
                bins[(i//digit) % 10].append(i)
            digit *= 10

            main = []
            for i in bins:
                while(len(i) > 0):
                    main.append(i.pop(0))
        return main
