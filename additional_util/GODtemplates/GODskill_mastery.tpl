Group
{
	name = "All Groups"
	type = "list"

	Variable
	{
		name = "Include File"
		class = "static"
		type = "include"
		description = ""
		value = ""
		defaultValue = "database\Templates\TemplateBase\Skill_Base.tpl"
	}

	Variable
	{
		name = "Include File"
		class = "static"
		type = "include"
		description = ""
		value = ""
		defaultValue = "database\Templates\TemplateBase\Skill_PassiveModifier.tpl"
	}

	Group
	{
		name = "Header"
		type = "system"

		Variable
		{
			name = "ActorName"
			class = "variable"
			type = "string"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "Class"
			class = "static"
			type = "string"
			description = ""
			value = ""
			defaultValue = "Skill_Mastery"
		}

		Variable
		{
			name = "FileDescription"
			class = "variable"
			type = "string"
			description = ""
			value = ""
			defaultValue = ""
		}

		Group
		{
			name = "Properties"
			type = "list"

			Variable
			{
				name = "MasteryEnumeration"
				class = "picklist"
				type = "string"
				description = ""
				value = ""
				defaultValue = "MasterySpirit;MasteryNature;MasteryStealth;MasteryHunting;MasteryStorm;MasteryEarth;MasteryDefense;MasteryWarfare;MasteryDreams;MasteryRuneMaster;MasteryNeidan"
			}

		}

	}

}
