from testing import *

# filename = "english1.wav"

# with open(filename, 'rb') as f:
#     print(read_in_audio(f))


cd = make_class_array('/media/enigmaeth/My Passport/sounds_wav/')
print(cd.shape)
np.save('top_3_100_split_mfcc.npy', cd)  

mf = make_mean_mfcc_df('/media/enigmaeth/My Passport/sounds_wav/')
print(mf.shape)
np.save('top_3_100_split_y.npy', mf)  