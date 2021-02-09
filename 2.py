#显示欢迎信息
print('-'*10,'欢迎光临《魏国兴大战LV》','-'*10)
#显示身份选择的信息
print('请选择你的身份:')
print('\t1.魏国兴')
print('\t2.LV')
#游戏的身份选择
player_choose = input('请选择【1-2】：')
print('-'*60)
#根据选择给与不同信息
if player_choose == '1':
	print('你已经选择了1，你将以====> 魏国兴 <====的身份来进行游戏')
elif player_choose == '2':
    print('你已经选择了2，你个不要脸的，你将以====> 魏国兴 <====的身份来进行游戏')
else :
	print('你是个傻子吧')
#进入游戏
#玩家指标
player_life = 2 # 骚气值
player_attack = 2 #车技
#BOSS指标
boss_life = 11
boss_attack = 11
print('-'*60)
#显示玩家的信息
print(f'>>>魏国兴<<<,你的骚气值是 {player_life},你的车技是 {player_attack}')
#由于游戏选项是反复显示的 要把显示编辑到循环里
while True :
	print('-'*60)
	# 显示游戏选项
	print('请选择你要进行的操作:')
	print('\t1.开车')
	print('\t2.开高铁')
	print('\t2.开挖掘机')
	print('-'*60)
	player_choose = input('请选择你要进行的操作【1-3】：')
	#处理游戏操作结果
	if player_choose == '1' :
		player_life += 2
		player_attack += 2
		print('-'*60)
		print(f'恭喜你升级，你的骚气值是 {player_life},你的车技是 {player_attack}')
	elif player_choose == '2':
	    #玩家攻击BOSS
	    #减去BOSS的骚气值
		boss_life -= player_attack
		print('>>>魏国兴<<< 攻击了 >>>LV<<<')
		#检查BOSS是否死亡
		if boss_life <= 0 :
			print(f'>>>LV<<<,{player_attack},点伤害,重伤不治死亡，>>>魏国兴<<<胜利')
			#游戏结束
			break
		player_life -= boss_attack
		print('>>>魏国兴<<< 被 >>>LV<<< 攻击')
		if player_life <= 0 :
			print(f'你受到了 {boss_attack} 点伤害，重伤不治死了！GAME OVER')
			break
	elif player_choose == '3':
		 print('>>>魏国兴<<<扭头就跑，游戏结束')	
		 break
	else :
		print('你的输入 有误')	 	
    # if game_choose == '1' :
    #     player_life += 2
    #     player_attack += 2
    #     # 显示最新的信息
    #     # 打印一条分割线
    #     print('-'*66)
    #     # 显示玩家的信息（车技、骚气值）
    #     print(f'恭喜你升级了！，你现在的骚气值是 {player_life} , 你的车技是 {player_attack}')
    # elif game_choose == '2' :
    #     # 玩家攻击boss
    #     # 减去boss的骚气值，减去的骚气值应该等于玩家的车技
    #     boss_life -= player_attack 
    #     print('-'*66)
    #     print('->魏国兴<- 攻击了 ->LV<-')
    #     # 检查boss是否死亡
    #     if boss_life <= 0 :
    #         # boss死亡，player胜利，游戏结束
    #         print(f'->LV<-受到了 {player_attack} 点伤害，重伤不治死了，->魏国兴<-赢得了胜利！')
    #         # 游戏结束
    #         break
    #     player_life -= boss_attack 
    #     print(' ->LV<- 攻击了 ->魏国兴<-')
    #     # 检查玩家是否死亡
    #     if player_life <= 0 :
    #         # 玩家死亡
    #         print(f'你受到了 {boss_attack} 点伤害，重伤不治死了！GAME OVER')
    #         # 游戏结束
    #         break
    # elif game_choose == '3' :
    #     # 打印一条分割线
    #     print('-'*66)
    #     # 开挖掘机，退出游戏
    #     print('->魏国兴<-一扭头，撒腿就跑！GAME OVER')
    #     break
    # else :
    #     # 打印一条分割线
    #     print('-'*66)
    #     print('你的输入有误，请重新输入！')