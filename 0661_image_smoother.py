# pad the image so that we dont have to deal with edge cases
# (yeah, edge cases by its pure meaning)
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        h = len(img)
        w = len(img[0])

        img_p = [[0] * (w+2)]
        c_p   = [[0] * (w+2)]
        for i in range(h):
            img_p.append([0] + img[i] + [0])
            c_p.append([0] + [1] * w + [0])
        img_p.append([0] * (w+2))
        c_p.append([0] * (w+2))
        
        r = []

        for hi in range(h):
            ri = []
            for wi in range(w):
                s = sum(img_p[hi][wi:wi+3]) + sum(img_p[hi+1][wi:wi+3]) + sum(img_p[hi+2][wi:wi+3])
                c = sum(  c_p[hi][wi:wi+3]) + sum(  c_p[hi+1][wi:wi+3]) + sum(  c_p[hi+2][wi:wi+3])
                ri.append(s // c)
            r.append(ri)

        return r