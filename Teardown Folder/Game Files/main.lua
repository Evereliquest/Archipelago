#version 2 

#include "common.lua"
#include "game.lua"
#include "script/toolutilities.lua"
#include "script/include/player.lua"

pDisableTools = GetBoolParam("disabletools", false)
pBaseTools = GetBoolParam("basetools", false)
gCustomToolsChecked = false

valuableSound = nil
allToolsCheck = nil

function server.init()
	local enabled = GetInt("options.game.archipelago.enabled")
	local levelId = GetString("game.levelid")
	local sledge = ""
	local spraycan = ""
	local extinguisher = ""
	local blowtorch = ""
	local shotgun = ""
	local plank = ""
	local pipebomb = ""
	local gun = ""
	local bomb = ""
	local rocket = ""
	local booster = ""
	local leafblower = ""
	local wire = ""
	local turbo = ""
	local explosive = ""
	local rifle = ""
	local steroid = ""

	if enabled == 0 then
		sledge = GetBool ("savegame.mod.steam-3708322400.tool.sledge.enabled")
		spraycan = GetBool ("savegame.mod.steam-3708322400.tool.spraycan.enabled")
		extinguisher = GetBool ("savegame.mod.steam-3708322400.tool.extinguisher.enabled")
		blowtorch = GetBool ("savegame.mod.steam-3708322400.tool.blowtorch.enabled")
		shotgun = GetBool ("savegame.mod.steam-3708322400.tool.shotgun.enabled")
		plank = GetBool ("savegame.mod.steam-3708322400.tool.plank.enabled")
		pipebomb = GetBool ("savegame.mod.steam-3708322400.tool.pipebomb.enabled")
		gun = GetBool ("savegame.mod.steam-3708322400.tool.gun.enabled")
		bomb = GetBool ("savegame.mod.steam-3708322400.tool.bomb.enabled")
		rocket = GetBool ("savegame.mod.steam-3708322400.tool.rocket.enabled")
		booster = GetBool ("savegame.mod.steam-3708322400.tool.booster.enabled")
		leafblower = GetBool ("savegame.mod.steam-3708322400.tool.leafblower.enabled")
		wire = GetBool ("savegame.mod.steam-3708322400.tool.wire.enabled")
		turbo = GetBool ("savegame.mod.steam-3708322400.tool.turbo.enabled")
		explosive = GetBool ("savegame.mod.steam-3708322400.tool.explosive.enabled")
		rifle = GetBool ("savegame.mod.steam-3708322400.tool.rifle.enabled")
		steroid = GetBool ("savegame.mod.steam-3708322400.tool.steroid.enabled")
	end





	shared.enableValuables = not string.find(levelId, "sandbox") and not string.find(levelId, "ch_")
	initValuables()

	--Check if playing campaign level
	local id = GetString("game.levelid")
	local isMod = HasKey("game.mod")
	local campaign = gMissions[id] ~= nil or (string.sub(id, 1, 3) == "hub" and not isMod and not string.find(id, "sandbox"))
	if campaign then
		SetString("game.quicksavename", "quicksavecampaign")
	else
		SetString("game.quicksavename", "quicksave")
	end

	if gMissions[id] then
		SetInt("level.missionsScoreSum", getLevelScore(gMissions[id].level))
	end
	syncActivities(id, true, false)
	---syncModActivities()
	if isMod then
		local modId = GetString("game.mod")
		if modId == "dlc-artvandals" then
			SetPresence("dlc_artvandals")
		else
			SetPresence("mod")
		end
	else
		SetPresence(id)
	end

	server.defaultTools = {}
	if pBaseTools then
		server.defaultTools["sledge"] = { enabled = true }
		server.defaultTools["spraycan"] = { enabled = true }
		server.defaultTools["extinguisher"] = { enabled = true }
	else
		if not pDisableTools then
			local isCampaign = gMissions[id] ~= nil or (string.sub(id, 1, 3) == "hub")

			if isCampaign or not IsMultiplayer() then
				server.defaultTools = setupToolsAmmoScaling(gTools, gMissions, false)
			else
				server.defaultTools = setupToolsUpgradedFully()
			end
		end
	end
end

function server.setDefaultToolsForPlayer(player)
	for toolId,preset in pairs(server.defaultTools) do
		SetToolEnabled(toolId, preset.enabled, player)
		if preset.enabled and preset.ammo then
			SetToolAmmo(toolId, preset.ammo, player)
		end
	end
end

function server.handleCommand(cmd)
	if cmd == "quickload" then
		--After quickload, make sure valuables are consistent with savegame
		initValuables()
	end
end

function initValuables()
	local enabled = GetInt("options.game.archipelago.enabled")
	if shared.enableValuables then
		valuables = FindBodies("valuable", true)
		local valueMin = 10000
		local valueMax = 0
		local valueTotal = 0
		for i=1,#valuables do
			local id = GetTagValue(valuables[i], "valuable")
			local v = tonumber(GetTagValue(valuables[i], "value"))
			valueMin = math.min(valueMin, v)
			valueMax = math.max(valueMax, v)
			valueTotal = valueTotal + v
			if enabled == 0 then
				if GetBool("savegame.mod.steam-3708322400.valuable."..id) then
					Delete(valuables[i])
				end
			else
				if GetBool("savegame.valuable."..id) then
					Delete(valuables[i])
				end
			end
		end
		--print(#valuables .. " valuables worth $" .. valueTotal ..  " ($" .. valueMin .. "-$" .. valueMax .. ")")
		valuables = FindBodies("valuable", true)
		for i=1,#valuables do
			SetTag(valuables[i], "interact", "loc@GRAB_VALUABLE")
		end
	else
		local v = FindBodies("valuable", true)
		for i=1,#v do
			RemoveTag(v[i], "valuable")
			RemoveTag(v[i], "value")
		end
	end
end

function server.tick(dt)
	for p in PlayersAdded() do
		server.setDefaultToolsForPlayer(p)
		if IsToolEnabled("sledge", p) then
			SetPlayerTool("sledge", p)
		end
		if not IsPlayerHost(p) then
			RespawnPlayer(p)
		end
	end

	--Check if we're in sandbox mode and all tools should be onlocked
	--This cannot be done in init, since we don't know the init order
	if not allToolsCheck then
		if GetBool("level.sandbox") and GetBool("level.unlimitedammo") and GetInt("options.game.sandbox.unlocktools") == 1 then
			for id,tool in pairs(gTools) do
				SetBool("game.tool."..id..".enabled", true, true)
			end
		end
		allToolsCheck = true
	end

	-- check custom tools on first tick after all mods inited
	if not gCustomToolsChecked then
		gCustomToolsChecked = true
		---syncCustomToolsActivities()
	end

	--Handle valuables
	if shared.enableValuables then
		for p in Players() do
			local interactPressed = InputPressed("interact", p)
			local interactBody = GetPlayerInteractBody(p)
			for i=1, #valuables do
				local s = valuables[i]
				if s ~= 0 and IsHandleValid(s) then
					--Remove if broken
					if IsBodyBroken(s) then
						RemoveTag(s, "valuable")
						RemoveTag(s, "interact")
						valuables[i] = 0
					end

					--Set text when language changed
					if interactBody == s then
						SetTag(s, "interact", "loc@GRAB_VALUABLE")
					end

					--Clear if interacted
					if interactBody == s and interactPressed then
						local enabled = GetInt("options.game.archipelago.enabled")
						local id = GetTagValue(s, "valuable")
						if enabled == 0 then
							SetBool("savegame.mod.steam-3708322400.valuable."..id, true);
						else
							SetBool("savegame.valuable."..id, true);
						end
						local value = tonumber(GetTagValue(s, "value"))
						if not value then value = 0 end
						if enabled == 0 then
							SetInt("savegame.mod.steam-3708322400.cash", GetInt("savegame.mod.steam-3708322400.cash") + value)
						else
							SetInt("savegame.cash", GetInt("savegame.cash") + value)
						end
						local msg = GetTranslatedStringByKey("UI_HUD_NOTE_PICKED_UP," .. GetDescription(s) .. "," .. value)
						ClientCall(0, "client.pickup", msg, p)
						Delete(s)
					end
				end
			end
		end
	end
end

----------------------------------------------------------------------------------------------------------

function client.init()
	if shared.enableValuables then
		valuables = FindBodies("valuable", true)
		valuableAlpha = {}
		valuableSound = LoadSound("valuable.ogg")
	end
end


function client.pickup(msg, p)
	if not IsPlayerLocal(p) then
		msg = GetPlayerName(p) .. " " .. msg
	end
	SetString("hud.notification", msg)
	PlaySound(valuableSound, GetCameraTransform().pos, 1.0, false)
end


function client.tick(dt)
	if shared.enableValuables then
		for p in Players() do
			for i=1, #valuables do
				local s = valuables[i]
				if s ~= 0 and IsHandleValid(s) then
					--Outline and picking info
					if IsBodyVisible(s, 6) then
						if valuableAlpha[s] == nil then
							valuableAlpha[s] = 1
						end
					else
						valuableAlpha[s] = nil
					end
					if valuableAlpha[s] then
						valuableAlpha[s] = valuableAlpha[s] - GetTimeStep()*2
						if valuableAlpha[s] > 0 then
							DrawBodyHighlight(s, valuableAlpha[s])
						end
					end
				end
			end
		end
	end
end

