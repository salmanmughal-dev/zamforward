with open('public/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace technical status steps with intuitive, friendly customer milestones
old_steps = '''const STATUS_STEPS = [
  { key: 'Confirmed', label: 'Order File Created', sub: 'Specs Registered' },
  { key: 'Received by ZAM', label: 'Received by ZAM', sub: 'Atelier Queued' },
  { key: 'Invoice Cleared', label: '50% Deposit Cleared', sub: 'Slip Verified' },
  { key: 'In Progress', label: 'In Progress', sub: 'Cut Scheduled' },
  { key: 'Production', label: 'Sublimation & Sewing', sub: 'Active in Atelier' },
  { key: 'Dispatched', label: 'QC & Dispatched', sub: 'DHL In Transit' },
  { key: 'Completed', label: 'Door Delivery', sub: 'Order Completed' }
];'''

new_steps = '''const STATUS_STEPS = [
  { key: 'Confirmed', label: 'Order Placed', sub: 'Received by ZamForward' },
  { key: 'Received by ZAM', label: 'Order Approved', sub: 'Specs Verified' },
  { key: 'Invoice Cleared', label: 'Deposit Cleared', sub: 'Payment Confirmed' },
  { key: 'In Progress', label: 'Scheduled', sub: 'Cut Scheduled' },
  { key: 'Production', label: 'Making Your Gear', sub: 'Printing & Sewing' },
  { key: 'Dispatched', label: 'Shipped', sub: 'On the Way (DHL)' },
  { key: 'Completed', label: 'Delivered', sub: 'Delivered to Your Door' }
];'''

text = text.replace(old_steps, new_steps)

# Replace technical phrases in quick modal
text = text.replace('ZamOne Atelier Engine', 'ZamForward Team Gear')
text = text.replace('Order Custom Combat Garment', 'Customize Your Fight Gear')
text = text.replace('Configure your combat kit, upload custom vectors or logos, and send file directly to ZamForward.', 'Choose your product, pick sizes and colors, and upload your team logo.')

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Status steps and modal updated with intuitive human-friendly language.")
