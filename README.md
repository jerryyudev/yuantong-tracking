# Yuantong Tracking Program

This is a Python program that allows users to query tracking information for Yuantong Express. It retrieves the latest shipment status and formats the information in a readable manner.

## Features

- Track Yuantong Express parcels.
- Displays the tracking information with timestamps in a human-readable format.
- Easy to use: Simply input the tracking number and get real-time updates.

## How to Use

1. **Install Python**: Make sure you have Python 3.x installed on your system.
   - You can download Python from [here](https://www.python.org/downloads/).

2. **Clone the repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/yuantong-tracking.git

3.**Install required libraries**: The program uses requests and subprocess to fetch and handle data. Install any necessary dependencies (if applicable):
   pip install requests

4.**Run the script**: Navigate to the directory where you downloaded the repository and run the script:
   python yt.py

5.**Enter tracking number**: When prompted, enter the tracking number for the Yuantong parcel you wish to track.

6.**View the tracking status**: The program will display the tracking information with timestamps and descriptions.

**Example**

请输入圆通快递单号: YT7520600652620

时间: 2025-01-17 15:27:45，描述: 您的快件离开【北京转运中心】，已发往【北京市朝阳区樱花园】
时间: 2025-01-17 14:52:39，描述: 您的快件已经到达【北京转运中心】
...

**Dependencies**
requests - for making HTTP requests.
subprocess - for running external commands like curl.

**License**
This project is open source and available under the MIT License.
