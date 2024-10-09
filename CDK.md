> Infrastructure as code solutions for AWS
1. AWS CloudFormation
2. AWS Serverless Application Model (SAM)
3. AWS Cloud Development Kit (CDK)  

> CDK Commands
1. cdk version
2. cdk init TEMPLATE --language LANGUAGE
3. ccdk bootstgrap # bootstrap the AWS environment
4. cdk list # list of stacks
5. cdk deploy
6. cdk destroy
7. cdk docs
8. cdk diff
9. cdk deploy --profile PROFILE_NAME #deploy with a specified profile
10. cdk deploy STACK_NAME # specify a stack to deploy
11. cdk deploy STACK_NAME_1, STACK_NAME_2
12. cdk deploy "*" #action be performed against all stacks in the app
13. 



> install CDK
```sh
* node --version
* npm install -g aws-cdk
* npm ls -g typescript
```

> AWS infrastructure with TypeScript: Getting Started
```ts
* cdk --version
* npm install aws-cdk -g
* cdk init app --language=typescript // creating new CDK application

//cdk.json //defines where the entry point is (the /bin/typescript-cdk.ts)
//package.json
//tsconfig.json
///bin/typescript-cdk.ts //where the application start
// here we create app and create instance of stack to app. stack file is under /lib
///lib
```