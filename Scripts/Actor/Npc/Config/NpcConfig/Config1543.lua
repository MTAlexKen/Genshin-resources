local L0_1, L1_1, L2_1, L3_1, L4_1, L5_1, L6_1, L7_1, L8_1, L9_1, L10_1, L11_1, L12_1, L13_1, L14_1, L15_1, L16_1
L0_1 = require
L1_1 = "Actor/ActorCommon"
L0_1(L1_1)
L0_1 = require
L1_1 = "Actor/Npc/Config/NpcConfigCommon"
L0_1 = L0_1(L1_1)
L1_1 = L0_1.GeneralPattern
L2_1 = L0_1.DailyCondition
L3_1 = L0_1.QuestState
L4_1 = L0_1.ActionPointType
L5_1 = L0_1.CompareOperation
L6_1 = {}
L7_1 = {}
L7_1.NpcId = "1543"
L7_1.Alias = "Npc1543"
L8_1 = {}
L9_1 = {}
L10_1 = {}
L11_1 = L2_1.Day
L10_1.daily = L11_1
L10_1.sceneId = 3
L10_1.priority = 0
L9_1.condition = L10_1
L10_1 = {}
L11_1 = {}
L12_1 = {}
L13_1 = {}
L13_1.x = 1973.039
L13_1.y = 210.3581
L13_1.z = -874.8248
L12_1.pos = L13_1
L13_1 = {}
L13_1.x = 0
L13_1.y = 134.7524
L13_1.z = 0
L12_1.rot = L13_1
L11_1.dummypoint = L12_1
L11_1.freestyle = 4010
L11_1.time = 40
L12_1 = L1_1.Stand
L11_1.action = L12_1
L12_1 = {}
L13_1 = {}
L14_1 = {}
L14_1.x = 1979.213
L14_1.y = 209.334
L14_1.z = -872.6915
L13_1.pos = L14_1
L14_1 = {}
L14_1.x = 0
L14_1.y = 284.14
L14_1.z = 0
L13_1.rot = L14_1
L12_1.dummypoint = L13_1
L13_1 = L1_1.Patrol
L12_1.action = L13_1
L13_1 = {}
L14_1 = {}
L15_1 = {}
L15_1.x = 1984.107
L15_1.y = 207.6115
L15_1.z = -866.5498
L14_1.pos = L15_1
L15_1 = {}
L15_1.x = 0
L15_1.y = 188.08
L15_1.z = 0
L14_1.rot = L15_1
L13_1.dummypoint = L14_1
L14_1 = L1_1.Patrol
L13_1.action = L14_1
L14_1 = {}
L15_1 = {}
L16_1 = {}
L16_1.x = 1985.087
L16_1.y = 203.9503
L16_1.z = -851.7173
L15_1.pos = L16_1
L16_1 = {}
L16_1.x = 0
L16_1.y = 81.4
L16_1.z = 0
L15_1.rot = L16_1
L14_1.dummypoint = L15_1
L14_1.freestyle = 4010
L14_1.time = 40
L15_1 = L1_1.Stand
L14_1.action = L15_1
L10_1[1] = L11_1
L10_1[2] = L12_1
L10_1[3] = L13_1
L10_1[4] = L14_1
L9_1.actionPoints = L10_1
L10_1 = {}
L11_1 = {}
L12_1 = L2_1.Night
L11_1.daily = L12_1
L11_1.sceneId = 3
L11_1.priority = 0
L10_1.condition = L11_1
L11_1 = {}
L12_1 = {}
L13_1 = {}
L14_1 = {}
L14_1.x = 1962.679
L14_1.y = 211.24
L14_1.z = -905.7246
L13_1.pos = L14_1
L14_1 = {}
L14_1.x = 0
L14_1.y = 289.6572
L14_1.z = 0
L13_1.rot = L14_1
L12_1.dummypoint = L13_1
L12_1.freestyle = 4151
L13_1 = L1_1.Stand
L12_1.action = L13_1
L11_1[1] = L12_1
L10_1.actionPoints = L11_1
L8_1[1] = L9_1
L8_1[2] = L10_1
L7_1.DailyScheduleData = L8_1
L6_1.Data = L7_1
return L6_1
