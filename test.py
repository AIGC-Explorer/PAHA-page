# Import the moviepy video editing library  
from moviepy.editor import VideoFileClip  

# Define the input and output file paths  
input_video_path = "/data/zsz/ssh/zsz/work/PAHA-page/static/video/3384.mp4"  # Replace with your actual input video path  
output_video_path = "/data/zsz/ssh/zsz/work/PAHA-page/static/video/resized_video.mp4"  # Replace with your desired output video path and filename  

# Define the desired resolution  
new_width = 512  
new_height = 896  

try:  
    # Load the video clip  
    video_clip = VideoFileClip(input_video_path)  

    # Resize the video  
    resized_video_clip = video_clip.resize((new_width, new_height))  

    # Write the resized video to the output file  
    resized_video_clip.write_videofile(output_video_path, codec="libx264")  # You can adjust the codec as needed  

    # Close the video clips to release resources  
    video_clip.close()  
    resized_video_clip.close()  

    print(f"Video successfully resized to {new_width}x{new_height} and saved to {output_video_path}")  

except Exception as e:  
    print(f"An error occurred: {e}")  