<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="numeric-textbox/identifier" />
        <xsl:variable name="minValue" select="numeric-textbox/min-value"/>
        <xsl:variable name="maxValue" select="numeric-textbox/max-value"/>
        
        <div class="container">
            <div class="form-group">
                
                <label for="{$identifier}">
                    <xsl:value-of select="numeric-textbox/label"/> 
                </label>
                
                <input type="number" class="form-control form-control-sm" 
                       id="{$identifier}" min="{$minValue}" max="{$maxValue}"/>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="numeric-textbox/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
