<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs math xd"
    version="3.0">
    
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex="((\d{{1,2}})\s([A-Za-z]+)(\.))">
            <xsl:matching-substring>
                <date><xsl:value-of select="regex-group(1)"/></date>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
<!--    Creates "date" tages around dates (that are formatted as: (d)d Month.) - EL-->    
    
    <xsl:template match="(p[contains(., 'Journal')])">
        <xsl:analyze-string select="." regex="(Journal)">
            <xsl:matching-substring>
                <journal><xsl:value-of select="regex-group(1)"/></journal>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!--Creates "journal" tags at any mention of a "Journal" - EL-->
    
    <xsl:template match="(p[contains(., 'JOURNAL')])">
        <xsl:analyze-string select="." regex="(JOURNAL)">
            <xsl:matching-substring>
                <journal><xsl:value-of select="regex-group(1)"/></journal>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!--Creates "journal" tags at any mention of a "JOURNAL" - EL-->
    
    <xsl:template match="(p[contains(., 'Diary')])">
        <xsl:analyze-string select="." regex="(Diary)">
            <xsl:matching-substring>
                <diary><xsl:value-of select="regex-group(1)"/></diary>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!--Creates "diary" tags at any mention of a "Diary" - EL-->
    
    <xsl:template match="(p[contains(., 'DIARY')])">
        <xsl:analyze-string select="." regex="(DIARY)">
            <xsl:matching-substring>
                <diary><xsl:value-of select="regex-group(1)"/></diary>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!--Creates "diary" tags at any mention of a "DIARY" - EL-->
    
    <xsl:template match="(p[contains(., '(')])">
        <xsl:analyze-string select="." regex="(\((.+?)\))">
            <xsl:matching-substring>
                <paren><xsl:value-of select="regex-group(1)"/></paren>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!--Creates "paren" tags anywhere where there are extra parenthetical descriptors - EL-->
    
    <xsl:template match="(p[contains(., 'Dracula')])">
        <xsl:analyze-string select="." regex="(Dracula)">
            <xsl:matching-substring>
                <dracula><xsl:value-of select="regex-group(1)"/></dracula>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/> 
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <!--Makes tages for anytime where Dracula is mentioned directly within the text - EL-->
</xsl:stylesheet>