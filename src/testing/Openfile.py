from aicspylibczi import CziFile
czi = CziFile("../data/EGFP-RAB7a+mCh-Perox-01.czi")

image_array = czi.read_image()