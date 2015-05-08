
def coords(fits):
    im = pyfits.open(fits)
    data = im[0].data
    
    ccd = PyGuide.CCDInfo(200,21.3,1.6) #Since we're using it on one CCD, these should be constants
    ctr,imstat = PyGuide.findStars(data,None,None,ccd,1,False)[0:2] #need to choose mask here
    
    xcoord = ['XCoord']
    ycoord = ['YCoord']
    names = ['StarName']
    size = np.array(ctr).size
    
    for x in range(0,size):
        xcoord = np.append(xcoord, ctr[x].xyCtr[0])
        ycoord = np.append(ycoord, ctr[x].xyCtr[1])
        names = np.append(names, x)
        
    one = xcoord.reshape((size + 1,1))
    two = ycoord.reshape((size + 1,1))
    thr = names.reshape((size + 1,1))
    guideData = np.hstack((thr,one,two))
    
    return guideData
