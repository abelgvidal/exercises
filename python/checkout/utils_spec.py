from expects import expect, equal, raise_error
from utils import grouper


with description('testing grouper'):

    with it('group 5 items in groups of 2'):
        groups = grouper(2, range(0,5))
        groups = list(groups)
        expect(len(groups)).to(equal(3))
        expect(len(groups[0])).to(equal(2))
        expect(len(groups[1])).to(equal(2))
        expect(len(groups[2])).to(equal(1))        

    with it('group 1 items in groups of 1'):
        groups = grouper(1, range(0,1))
        groups = list(groups)
        expect(len(groups)).to(equal(1))

    with it('group 1 items in groups of 2'):
        groups = grouper(1, range(0,1))
        groups = list(groups)
        expect(len(groups)).to(equal(1))
        expect(len(groups[0])).to(equal(1))

    with it("when a decimal or < 1 n is passed, it fails"):
        def c_neg():
            next(grouper(-1, range(0,3)))
        def c_dec():
            next(grouper(0.222, range(0,3)))
        def c_zer():
            next(grouper(0, range(0,3)))
        def c_non():
            next(grouper(None, range(0,3)))

        for callback in [c_neg, c_dec, c_zer, c_non]:
            expect(callback).to(raise_error(ValueError))
            
    
