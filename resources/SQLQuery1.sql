
INSERT INTO [dbo].[AgentHostName] ([name], [bpaagentname])
VALUES ('TESTPCBEVDAPRGTLS01', '1-PCBEVDAPRGTLS01');
INSERT INTO [dbo].[AgentHostName] ([name], [bpaagentname])
VALUES ('TESTPCBEVDAPRGTLS02', '2-PCBEVDAPRGTLS01');
INSERT INTO [dbo].[AgentHostName] ([name], [bpaagentname])
VALUES ('TESTPCBEVDAPRGTLS03', '3-PCBEVDAPRGTLS01');

INSERT INTO [dbo].[Client] ([name])
VALUES ('CIBC');
INSERT INTO [dbo].[Client] ([name])
VALUES ('DESJ');

INSERT INTO [dbo].[Environment] ([name])
VALUES ('PROD');
INSERT INTO [dbo].[Environment] ([name])
VALUES ('DIRC');

INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1004, '2020-05-13 00:47:25', 1, 2);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1006, '2020-05-13 00:47:25', 2, 1);

INSERT INTO [dbo].[Technology] ([name])
VALUES ('Genesys');
INSERT INTO [dbo].[Technology] ([name])
VALUES ('NewT');


INSERT INTO [dbo].[Workflow] ([name], [technologyid])
VALUES ('WORKF 1', 1);
INSERT INTO [dbo].[Workflow] ([name], [technologyid])
VALUES ('WORKF 2', 2);

INSERT INTO [dbo].[Trigger] ([name])
VALUES ('Auto');
INSERT INTO [dbo].[Trigger] ([name])
VALUES ('Manual');

INSERT INTO [dbo].[Task] ([name], [workflowid])
VALUES ('Task 1', 1);
INSERT INTO [dbo].[Task] ([name], [workflowid])
VALUES ('Task 2', 2);

INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 1', 1);
INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 2', 2);

INSERT INTO [dbo].[State] ([name])
VALUES ('Succeed');
INSERT INTO [dbo].[State] ([name])
VALUES ('Failed');

INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid], [description])
VALUES (1,2, '2020-05-19 00:32:25', '2020-05-19 01:33:25', 1, 2, 'desc sentence');
INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid], [description])
VALUES (2,2, '2020-05-12 00:47:25', '2020-05-12 01:45:25', 2, 1, 'desc result');

INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (1,'Result -1- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (2,'Result -2- details');

INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (1,1);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (2,2);


INSERT INTO [dbo].[AgentHostName] ([name], [bpaagentname])
VALUES ('TESTPCBEVDAPRGTLS03', '3-PCBEVDAPRGTLS01');
INSERT INTO [dbo].[AgentHostName] ([name], [bpaagentname])
VALUES ('TESTPCBEVDAPRGTLS04', '4-PCBEVDAPRGTLS01');
INSERT INTO [dbo].[AgentHostName] ([name], [bpaagentname])
VALUES ('TESTPCBEVDAPRGTLS05', '5-PCBEVDAPRGTLS01');

INSERT INTO [dbo].[Client] ([name])
VALUES ('Client 3');
INSERT INTO [dbo].[Client] ([name])
VALUES ('Client 4');
INSERT INTO [dbo].[Client] ([name])
VALUES ('Client 5');

INSERT INTO [dbo].[Environment] ([name])
VALUES ('ENV 3');
INSERT INTO [dbo].[Environment] ([name])
VALUES ('ENV 4');
INSERT INTO [dbo].[Environment] ([name])
VALUES ('ENV 5');

INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1007,'2020-05-13 00:47:25', 3, 3);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1009,'2020-05-13 00:47:25', 4, 4);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1010,'2020-05-13 00:47:25', 5, 5);

INSERT INTO [dbo].[Technology] ([name])
VALUES ('Tech 3');
INSERT INTO [dbo].[Technology] ([name])
VALUES ('Tech 4');
INSERT INTO [dbo].[Technology] ([name])
VALUES ('Tech 5');


INSERT INTO [dbo].[Workflow] ([name], [technologyid])
VALUES ('WORKF 3', 3);
INSERT INTO [dbo].[Workflow] ([name], [technologyid])
VALUES ('WORKF 4', 4);
INSERT INTO [dbo].[Workflow] ([name], [technologyid])
VALUES ('WORKF 5', 5);

INSERT INTO [dbo].[Trigger] ([name])
VALUES ('Auto');
INSERT INTO [dbo].[Trigger] ([name])
VALUES ('Manual');

INSERT INTO [dbo].[Task] ([name], [workflowid])
VALUES ('Task 3', 3);
INSERT INTO [dbo].[Task] ([name], [workflowid])
VALUES ('Task 4', 4);
INSERT INTO [dbo].[Task] ([name], [workflowid])
VALUES ('Task 5', 5);

INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 3', 3);
INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 4', 4);
INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 5', 5);

INSERT INTO [dbo].[State] ([name])
VALUES ('Succeed');
INSERT INTO [dbo].[State] ([name])
VALUES ('Failed');
INSERT INTO [dbo].[State] ([name])
VALUES ('Warning');

INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid])
VALUES (1,2, '2020-05-18 00:32:25', '2020-05-18 01:33:25', 3, 2);
INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid])
VALUES (2,2, '2020-05-15 00:47:25', '2020-05-15 01:45:25', 2, 2);
INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid])
VALUES (2,2, '2020-05-16 00:47:25', '2020-05-16 01:45:25', 2, 1);

INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (1,'Result -1- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (2,'Result -2- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (3,'Result -3- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (4,'Result -4- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (5,'Result -5- details');

INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (1,1);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (2,2);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (3,3);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (4,4);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (5,5);

INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1007,'2020-05-13 00:47:25',1, 3);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1006,'2020-05-13 00:47:25', 1, 4);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1010,'2020-05-13 00:47:25', 2, 3);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1010,'2020-05-13 00:47:25', 2, 4);

INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 6', 3);
INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 7', 4);
INSERT INTO [dbo].[Test] ([name], [taskid])
VALUES ('Test 8', 5);

INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid])
VALUES (6,6, '2020-05-18 00:32:25', '2020-05-18 01:33:25', 5, 2);
INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid])
VALUES (7,7, '2020-05-15 00:47:25', '2020-05-15 01:45:25', 2, 2);
INSERT INTO [dbo].[Resultdetail] ([resultid], [testid],[starttime],[endtime], [stateid], [triggerid])
VALUES (9,8, '2020-05-16 00:47:25', '2020-05-16 01:45:25', 2, 1);

INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (5,'Result -6- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (7,'Result -7- details');
INSERT INTO [dbo].[ResultDetailText] ([resultdetailid], [details])
VALUES (10,'Result -10- details');

select * from ResultDetail

INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (1,3);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (1,2);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (2,3);
INSERT INTO [dbo].[ClientWorkflow] ([clientId], [workflowid])
VALUES (2,4);

INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1009, GETDATE(), 3, 3);
INSERT INTO [dbo].[Result] ([agentid], [executiondate],[clientid],[environmentid])
VALUES (1006, GETDATE(), 4, 2);