import numpy as np



def Conv2D(input, filter, bias, stride=2):
    row = input_.shape[0]-filter_.shape[0] + 1
    col = input_.shape[1]-filter_.shape[1] + 1
    result2 = []
    for r in range(row):
        for c in range(col):
            result1 = input_[r:r+filter_.shape[0],c:c+filter_.shape[1]]*filter_
            result2.append(np.sum(result1)+bias)
        print(result2)
    
    result = np.array(result2).reshape(row,col)
    return result


def im2col(input, filter, stride=1,pad=0):
    N, C, H, W = input.shape
    filter_h , filter_w = filter.shape
    out_h = (H + 2 * pad - filter.shape[0])//stride + 1
    out_w = (W + 2 * pad - filter.shape[0])//stride + 1

    img = np.pad(input,[(0,0),(0,0),(pad,pad),(pad,pad)],'constant')
    print(img)
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
    for y in range(filter_h):
        y_max = y + stride * out_h
        for x in range(filter_w):
            x_max = x + stride * out_w
            col [:,:,y,x,:,:] = img[:,:,y:y_max:stride,x:x_max:stride]

    return col.transpose(0,4,5,1,2,3).reshape(N*out_h*out_w,-1)



input_ = np.array(
    [[
    # [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,0]],
    # [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,0]],
    # [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,0]]
    [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
    [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]],
    [[3,3,3,3],[3,3,3,3],[3,3,3,3],[3,3,3,3]]
    ]]
    )
filter_ = np.array(
    [[
    [[1,1,1],[2,2,2],[3,3,3]]
    ]
    )
bias = 3
print(input_.shape)

# input_pad = np.pad(input_, pad_width=2, mode='constant', constant_values=0)

temp = im2col(input_,filter_, pad=1)
print(temp)
print(temp.shape)




