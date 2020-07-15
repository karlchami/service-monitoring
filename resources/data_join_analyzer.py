import glob
import json

def merge_json(output_path):
    try:
        print("Merging files, please wait...")
        read_files = glob.glob('\\\Dc6c3t\d$\Bellfit09\DecryptedFiles\CcsoChecklists\*\*.json')
        with open(output_path, "wb") as outfile:
            outfile.write('[{}]'.format(
                ','.join([open(f, "rb").read() for f in read_files])))
        print("Successful.")        
    except Exception as e:
        print(str(e))

def select_distinct(field_name):
    try:
        with open(output_path) as f:
            content = json.load(f)

        values = set()
        for item in content:
            values.add(item[field_name])

        values = set([i[field_name] for i in content])
        print field_name + ': \n', ' // '.join(values)
        print("\n")
    except Exception as e:
        print(str(e) + ". Make sure the JSON file is valid.")    

output_path = "C:\Users\karljoey.chami\Desktop\JSON_DATA_SCRIPTS\merged_result\merged_file.json"
merge_json(output_path)

print("Analyzing data...")

select_distinct('Client')
select_distinct('Technology')
select_distinct('Environment')
select_distinct('AgentHostname')
select_distinct('BPA_AgentName')
select_distinct('BPA_Workflow')
select_distinct('BPA_TaskName')
select_distinct('BPA_Trigger')
select_distinct('TestName')
select_distinct('State')
