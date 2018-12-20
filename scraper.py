import json
from collections import defaultdict
import datetime
import matplotlib.pyplot as plt
import operator

senderName = "Birry William Pan"
recieverName = "Jessica Tran"

messageDateDic = defaultdict(int)
messageDateDicSender = defaultdict(int)
messageDateDicReciever = defaultdict(int)

messageMonthDic = defaultdict(int)
messageMonthDicSender = defaultdict(int)
messageMonthDicReciever = defaultdict(int)

messageCountSender = 0
messageCountReciever = 0

with open('message.json') as data_file:
    messages = json.load(data_file)
    for msg in messages["messages"]:
        # For text messages
        if msg["type"] == "Generic":
            time = datetime.datetime.fromtimestamp(float(msg["timestamp_ms"])/1000.0)
            messageDateDic[time.date()] += 1
            messageMonthDic[time.month] += 1
            if msg["sender_name"] == senderName:
                messageCountSender += 1
                messageDateDicSender[time.date()] += 1
                messageMonthDicSender[time.month] += 1
            else:
                messageCountReciever += 1
                messageDateDicReciever[time.date()] += 1
                messageMonthDicReciever[time.month] += 1

sortedMessageDateData = sorted(messageDateDic.items())

sortedMessageMonthData = sorted(messageMonthDic.items())

sortedMessageDateSenderData = sorted(messageDateDicSender.items())
sortedMessageDateRecieverData = sorted(messageDateDicReciever.items())

sortedMessageMonthSenderData = sorted(messageMonthDicSender.items())
sortedMessageMonthRecieverData = sorted(messageMonthDicReciever.items())

# Statistics
print("Total Messages sent by sender: " + str(messageCountSender))
print("Total Messages sent by reciever: " + str(messageCountReciever))

# Plot monthly data
plt.figure(1)
x, y = zip(*sortedMessageMonthData)
plt.plot(x, y)

# Plot monthly data per person
plt.figure(2)
x, y = zip(*sortedMessageMonthSenderData)
plt.plot(x, y, label="Sender")
x, y = zip(*sortedMessageMonthRecieverData)
plt.plot(x, y)
plt.plot(x, y, label="Reciever")
plt.legend(loc='upper right')

# Plot daily data
plt.figure(3)
x, y = zip(*sortedMessageDateData)
plt.plot(x, y)

# Plot daily data per person
plt.figure(4)
x, y = zip(*sortedMessageDateSenderData)
plt.plot(x, y, label="Sender")
x, y = zip(*sortedMessageDateRecieverData)
plt.plot(x, y, label="Reciever")
plt.legend(loc='upper right')

plt.show()
