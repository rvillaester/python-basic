import boto3

session = boto3.Session(profile_name='mac')
ec2 = session.resource('ec2', verify=False)
s3 = session.resource('s3', verify=False)

def s3Test():
    for bucket in s3.buckets.all():
        print(bucket.name)

def createEc2Intance():
    ec2.create_instances(ImageId='ami-02d039674ab9ba947', InstanceType='t2.micro', MinCount=1, MaxCount=1)

def listEc2Instances():
    for i in ec2.instances.all():
        print(i.id, i.state['Name'])

def stopEc2Instances():
    for i in ec2.instances.all():
        print(i.stop())

def startEc2Instances():
    for i in ec2.instances.all():
        print(i.start())

def terminateEc2Instances():
    for i in ec2.instances.all():
        print(i.terminate())

terminateEc2Instances()
listEc2Instances()